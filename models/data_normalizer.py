import requests

def normalize_clinical_data(raw_data):
    # 假设 ollama API 的 URL 和端点如下
    api_url = "http://ollama.api.com/normalize"
    
    # 请求体中包含需要规范化处理的原始数据
    payload = {
        "data": raw_data
    }
    
    # 设置请求头，如果需要的话
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer your_api_key_here"  # 如果需要认证
    }
    
    # 发送 POST 请求到 ollama API
    response = requests.post(api_url, json=payload, headers=headers)
    
    # 检查响应状态码，确保请求成功
    if response.status_code == 200:
        # 返回规范化后的数据
        return response.json()
    else:
        # 如果请求失败，抛出异常并打印错误信息
        raise Exception(f"Failed to normalize data: {response.status_code} - {response.text}")