
pb_include=-I $(shell go list -f '{{ .Dir }}/..' github.com/golang/protobuf/protoc-gen-go)
pb_include+=-I $(shell echo $$HOME/go/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis)
pb_include+=-I $(shell echo $$HOME/go/src/github.com/gogo/protobuf)/protobuf
pb_include+=-I $(shell echo $$HOME/go/src/github.com/grpc-ecosystem/grpc-gateway)/third_party/googleapis
proto: api/*.proto
	@echo "Rebuilding protobuf stubs"
	go get github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway
	go get github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger
	go get github.com/golang/protobuf/protoc-gen-go
	go get github.com/gogo/protobuf/protoc-gen-gofast
	protoc $< -I.\
	    $(pb_include) \
	    --swagger_out=. \
		--python_out=.
	    --go_out=paths=source_relative,plugins=grpc:.


