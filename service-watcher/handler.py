import wacher

# Lambdaはこの関数を呼び出す
def hello(event, context):
    watcher.watch("https://example.com")
