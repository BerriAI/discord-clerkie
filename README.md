# clerkie Discord Bot
## Introduction
Are you tired of scouring the internet for solutions to your programming errors? Look no further! clerkie is here to help. Simply invite clerkie to your Discord server and use the command !clerkie <StackTrace> to get help fixing your errors.

## Usage
To use clerkie, first invite the bot to your Discord server by following [this link](https://discord.com/api/oauth2/authorize?client_id=1061821735411908700&permissions=274877908992&scope=bot). Then, in any channel that clerkie has access to, type !clerkie followed by a copy of your stack trace. clerkie will do its best to provide a solution to your problem.

For example, if you have the following error:

```
TypeError: Cannot read property 'name' of undefined
    at Object.exports.run (C:\Users\MyUser\project\index.js:22:27)
    at C:\Users\MyUser\project\node_modules\discord.js\src\client\Client.js:628:24
    at C:\Users\MyUser\project\node_modules\discord.js\src\client\Client.js:622:11
    at C:\Users\MyUser\project\node_modules\discord.js\src\client\Client.js:557:14
    at processTicksAndRejections (internal/process/task_queues.js:97:5)
```


You would type 

!clerkie TypeError: Cannot read property 'name' of undefined at Object.exports.run (C:\Users\MyUser\project\index.js:22:27) at C:\Users\MyUser\project\node_modules\discord.js\src\client\Client.js:628:24 at C:\Users\MyUser\project\node_modules\discord.js\src\client\Client.js:622:11 at C:\Users\MyUser\project\node_modules\discord.js\src\client\Client.js:557:14 at processTicksAndRejections (internal/process/task_queues.js:97:5)


## Support
If you need further assistance or have any issues with the bot, please don't hesitate to reach out to us by opening a GitHub issue. We are here to help!
