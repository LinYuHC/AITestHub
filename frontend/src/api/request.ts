import axios from 'axios'

/*
xios.create()表示创建一个axios实例，并统一指定后端地址，方便维护。以后request.get('/api/v1/posts/list')，
实际访问地址为http://81.71.136.66:8000/api/v1/posts/list，
而timeout: 5000表示请求超时时间5秒。
*/
const BASE_URL = 'http://81.71.136.66:8000'
const local_BASE_URL = 'http://127.0.0.1:8000'
const request = axios.create({
  // baseURL: import.meta.env.VITE_API_BASE_URL,
  baseURL: local_BASE_URL,
  // baseURL: local_BASE_URL,
  timeout: 5000
})

// ==================================================
// Axios 请求拦截器
// ==================================================
//
// 每一次请求真正发送到 FastAPI 之前，
// 都会先经过这里。
//
// 我们在这里统一读取 Token，
// 并将 Token 添加到 Authorization 请求头。
// ==================================================
request.interceptors.request.use(
  (config) => {

    // 从浏览器 localStorage 获取已经登录的 JWT
    const token = localStorage.getItem('access_token')

    // 如果 Token 存在，就给当前请求添加 Authorization 请求头。
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }

    // 返回修改后的请求配置，Axios 拿到这个 config 后才真正发送请求。
    return config
  },

  (error) => {

    // 请求配置阶段发生错误
    return Promise.reject(error)

  }
)


export default request