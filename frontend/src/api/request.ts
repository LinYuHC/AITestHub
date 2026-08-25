import axios from 'axios'

/*
xios.create()表示创建一个axios实例，并统一指定后端地址，方便维护。以后request.get('/api/v1/posts/list')，
实际访问地址为http://81.71.136.66:8000/api/v1/posts/list，
而timeout: 5000表示请求超时时间5秒。
*/
const BASE_URL = 'http://81.71.136.66:8000'
const local_BASE_URL = 'http://127.0.0.1:8000'
const request = axios.create({
  baseURL: BASE_URL,
  // baseURL: local_BASE_URL,
  timeout: 5000
})

export default request