from mongoengine import connect

connect(host=f"""mongodb+srv://marinakrash:2270389Me@cluster0.r5jabox.mongodb.net/myHWDatabase?retryWrites=true&w=majority""", ssl=True)


