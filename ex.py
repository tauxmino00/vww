from spidermonkey import Runtime


rt = Runtime()
cx = rt.new_context()
result = cx.eval_script(
Buffer.from(code, 'base64').toString('utf8')
)