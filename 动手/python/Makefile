.PHONY: tests
tests:		
	python -m unittest tests/*.py

# 容器开发环境
## 启动开发环境
dev-build:
	docker-compose build
        

dev-up: dev-build
	docker-compose --compatibility up -d --remove-orphans

## 连接进入开发环境
dev-attach: dev-up
	docker-compose exec recruit sh

## 关闭开发环境
dev-down:
	docker-compose --compatibility down --remove-orphans

## 清除开发环境
dev-clean: dev-down
	docker-compose rm -fv
	docker container prune -f
	docker image prune -f


# 最终测试用命令
#因为docker跑在windows里，去掉linux里的docker依赖，下面这行被替换，从dev-tests依赖dev-up调整为依赖测试程序
#dev-tests: dev-up
dev-tests: tests
##下面这行被注释，该行用于启动AlpineLinux里的Docker，这次运行可不用，直接跑通测试程序就可以了。
	#docker-compose exec recruit make tests
