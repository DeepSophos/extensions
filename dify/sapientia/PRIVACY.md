## Privacy

### 1. Types of data collected

The plugin may collect and process the following types of user data during runtime:

#### Directly identify information

- No direct identification information is collected directly by the plugin.

#### Indirect identification information

- **IP Address**: The plugin communicates with a remote server through HTTP requests, and the server may record the IP address that initiated the request.
- **User inputted query content**: The plugin collects the query text entered by the user through the parameter 'text', which may include personal information entered by the user themselves.
- Access Token: The plugin uses a user provided 'token' and sends it to a remote server for authentication, which is provided by a third-party service.

#### Combination information
- No clear combination information is directly collected by the plugin.

#### Data collection for third-party services
The plugin makes HTTP requests to external servers` http://www.sapientia.work:43013 `Or user specified 'origin' interaction. The plugin itself does not directly store or process data.

### 2. Data usage

- Query Processing: The query text (` text `) and specified scope (` scopes `) entered by the user are used to send requests to remote servers to obtain relevant response data.
- **Authentication**: 
The access token provided by the user is used to verify the user's identity and ensure legitimate access to the remote server.
-Reference Processing: The plugin processes the response data returned by the server, extracts and formats the reference content (including image URLs), in order to display the processed results to the user.

### 3. data sharing

The plugin itself does not directly share user data with third parties. However, the plugin sends the following data to the user specified remote server via HTTP request (default:` http://www.sapientia.work:43013 `）：
- Query Text (` text `)
- Scope parameters (` scopes `)
- Access Token

These data are processed by remote servers.

### 4. third-party services

- **Remote Server**: The plugin makes HTTP requests to the server specified by the user (default:` http://www.sapientia.work:43013 `Interaction.
- **No other third-party services**: The plugin does not rely on other third-party services (such as Slack, Google, etc.) for data processing.

### 5. Data Storage and Protection

The plugin itself does not store any user data. All data processing is completed at runtime and sent to the remote server via HTTP requests.

### 6. user rights

Users can limit the data that plugins may collect by not providing sensitive information (such as avoiding including personal information in query text). Users can control the destination server and authentication method for data transmission by configuring 'Origin' and 'Token'.

### 7. contact information

If you have any questions about this privacy policy, please contact the plugin developer.

Shanghai Seek Time Technology Co., Ltd

21st Floor, No. 1, Lane 339, Tongpu Road, Putuo District, Shanghai, china

Github：https://github.com/DeepSophos/extensions