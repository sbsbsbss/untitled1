from loguru import logger

#
"""
调试日志:debug()10
一般日志:info()20
警告日志:wanging()30
成功日志:success()40
错误日志:error()50
"""
# logger.add('test.log',format="{time}{lefel}{message}",level='INFO')

logger.debug("这是一条debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")

logger.info("{}今年{}岁，喜欢吃{}","蔡子贤","25","西瓜")



