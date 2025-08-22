## SeekTime Super Rag Component

**Author:** SeekTime
**Version:** 0.0.2
**Type:** tool

### Description

The SeekTime Super Rag Component is a Dify plugin designed for the knowledge base Q&A product of Shanghai Seek-Time Technology Co., Ltd. Automatic and precise slicing of document materials, powerful multimodal chart understanding ability, high accuracy of Q&A, and precise traceability of answers to the specific location of the original text, allowing you to immediately have the world's leading AI knowledge base capability!

#### Main functions
- Query processing: Based on the query text and scope entered by the user, send a request to the remote server to obtain relevant knowledge base content.
- Reference formatting: Processing the reference content returned by the server, converting the reference anchor and target (such as image URL) into a user-friendly format.
- **Error Handling**: Capture and return error messages related to HTTP requests, JSON parsing, or other exceptions to ensure user experience.

#### Usage scenarios
- Enterprise Knowledge Base Q&A: Integrate the knowledge base system of Shanghai Qiusuo Time Technology Co., Ltd. to provide users with accurate Q&A services.
- Reference display: Present the reference content (such as images) in a visual way in the knowledge base to enhance the interactive experience.

#### Preconditions
- **Server Access**: Need to access the knowledge base server of Shanghai Qiusuo Time Technology Co., Ltd. (default address:` https://www.seek-time.com:43032 `).
- Access Token: Users need to access the knowledge base system of Shanghai Qiusuo Time Technology Co., Ltd. to obtain the access token.
- **Supported file formats**: The plugin processes server responses in JSON format, ensuring that the data format returned by the server is compatible.

#### Installation steps
1. **Obtain plugin**:
- Download the SeekTime Super Rag Component from Dify Marketplace.
- Reference [Shopify Plugin Development Document]（ https://docs.dify.ai/plugin-dev-zh ）Configure plugin environment.

2. **Configure plugins**:
- In the Dify platform, go to 'Studio' ->'Create Application' ->'Add Plugin'.
- Select the SeekTime Super Rag Component and add it to your application workflow.

3. **Set Parameters**:
- Configure the following parameters:
- Origin (optional): Remote server address, default value is` https://www.seek-time.com:43032 `.
- Token (required): The access token used for authentication.
- ` text ` (required): The query text entered by the user.
- 'scopes' (required): Query scope, a comma separated string (such as' scope1, scope2 ').

4. **Workflow Integration**:
- In the Dify workflow, place the SeekTime Super Rag Component node in the appropriate position (such as after the user inputs the node).
- Map user input variables (such as' sys. query ') to' text '.
- Configure downstream nodes to receive output from the SeekTime Super Rag Component (text messages or formatted reference content).

#### Example usage
##### Workflow configuration
1. Create a Dify chatbot application.
2. Add the SeekTime Super Rag Component node and set the parameters:
```json
{
"origin": " https://www.seek-time.com:43032 ",
"token": "your-access-token",
"text": "{{sys.query}}",
"scopes": "knowledge,faq"
}
```
3. Connect the output of SeekTime Super Rag Component to the LLM node or directly reply to the node to generate the final response.
4. Debug and release the application.

##### User interaction
- User input question: 'What is a knowledge base question answering system?'? `
- The plugin sends a request to the server to retrieve relevant knowledge base content.
- The plugin processes the returned reference content and generates formatted text and image links.
- Output example:
```
A knowledge base question answering system is an intelligent system that utilizes large-scale language models and knowledge base retrieval techniques to provide accurate answers. [1]
<img src=' https://www.seek-time.com:43032/agents/api/v1/pdf_image/12345 ' />
```

#### Precautions
- Privacy and Data Security: The plugin will send the query text and token entered by the user to the remote server. Please refer to the [Privacy Policy] (QueryTool-Privacy. Policy. md) for details on data processing and ensure compliance with the privacy policy of the target server.
- Server Dependency: Plugin functionality depends on the availability and response format of the remote server. Ensure that the server address is correct and the service is running smoothly.
- Error Handling: If an HTTP request fails or JSON parsing error occurs, the plugin will return a clear error message for easy debugging.

#### Frequently Asked Questions
How to obtain an access token?
- Please refer to the documentation of the knowledge base system of Shanghai Qiusuo Time Technology Co., Ltd. to obtain a valid access token.

#### Contact Information
If you need technical support or feedback, please contact the technical support team of Shanghai Qiusuo Time Technology Co., Ltd.
Github：https://github.com/DeepSophos/extensions