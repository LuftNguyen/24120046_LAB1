import uvicorn

if __name__ == "__main__":
    print("Đang khởi động Server FastAPI cho bài toán TSP...")
    
    # app:app có nghĩa là: tìm biến 'app' bên trong file 'app.py'
    # host="0.0.0.0" cho phép mạng bên ngoài (như Pinggy) truy cập vào server
    # port=8000 là cổng giao tiếp mặc định
    # reload=True giúp server tự khởi động lại mỗi khi bạn sửa code (rất tiện khi code ở Local)
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)