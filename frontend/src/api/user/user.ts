import request from "../request.ts";

// 登录
export function login(username: string, password: string) {
    return request.post('/api/v1/auth/login', {
        username: username,
        password: password
    })
}

// 退出登录
export function logout() {
    return request.post('/api/v1/auth/logout')
}

export function getUserInfo() {
    return request.get('/api/v1/auth/userinfo')
}