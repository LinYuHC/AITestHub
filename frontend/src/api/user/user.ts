import request from "../request.ts";

export function login(username: string, password: string) {
    return request.post('/api/v1/auth/login', {
        username: username,
        password: password
    })
}