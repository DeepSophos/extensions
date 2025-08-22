import requests
import json
import re
from collections.abc import Generator
from typing import Any
from time import sleep
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class QueryTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        self.origin = "https://www.seek-time.com:43032"
        if tool_parameters["origin"]:
            self.origin = tool_parameters["origin"]

        url = f"{self.origin}/agents/api/v1/query"
        headers = {
            "Authorization": tool_parameters["token"]
        }

        data = {
            "state": {
                "query": tool_parameters["text"],
                "scopes": tool_parameters["scopes"].split(',')
            }
        }

        try:
            response = requests.post(url, headers=headers, json=data, stream=True)
            response.raise_for_status()

            response_status = False
            for line in response.iter_lines():
                if line:
                    res_json = json.loads(line.decode('utf-8'))
                    if response_status and res_json["channel"] == "response" and res_json["command"] == "append":
                        yield self.create_text_message(self.handleCitation(str(res_json["data"])))
                    if res_json["command"] == "rewind":
                        response_status = True
        except requests.RequestException as e:
            yield self.create_text_message(f"HTTP 请求失败: {str(e)}")
        except json.JSONDecodeError as e:
            yield self.create_text_message(f"JSON 解析失败: {str(e)}")
        except Exception as e:
            yield self.create_text_message(f"未知错误: {str(e)}")

    def handleCitation(self, content):
        # 截去see also
        index = content.find("**See also**:")
        if index != -1:
            content = content[:index]

        def replace_citation_anchor(match):
            key = match.group(1)
            return f"[{key}]"

        def replace_citation_target(match):
            key = match.group(1)
            return f"<img src='{self.origin}/agents/api/v1/pdf_image/{key}' />"

        # 处理引用
        pattern_anchor = r'\[\[(\d+)\]\]'
        pattern_target = r'\(/rightpanel/citation-([^)]+)\)'
        # 处理引用
        content = re.sub(pattern_anchor, replace_citation_anchor, content)
        content = re.sub(pattern_target, replace_citation_target, content)
        return content
