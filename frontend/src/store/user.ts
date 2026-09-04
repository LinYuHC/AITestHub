import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { getUserInfo } from '../api/user/user'

export interface UserInfo {
    id: number
    username: string
    nickname?: string
    avatar?: string
}

// 用户信息 store
export const useUserStore = defineStore('user', () => {

    // 当前用户信息
    const userInfo = ref<UserInfo | null>(null)

    // 当前是否登录
    const isLogin = computed(() => {
        return userInfo.value !== null
    })

    // 登录成功后保存用户信息
    const setUserInfo = (user: UserInfo) => {
        userInfo.value = user
    }

    // ==============================
    // 初始化登录状态
    // ==============================
    const initUser = async () => {

        // 先检查浏览器有没有保存 Token
        const token = localStorage.getItem('access_token')

        // 没有 Token，说明没有登录
        if (!token) {
            console.log('没有Token，不恢复登录状态')
            userInfo.value = null
            return
        }

        try {
            console.log('开始调用获取当前用户接口')

            // 有 Token，向后端获取当前用户信息
            const response = await getUserInfo()
            console.log('获取当前用户接口完整响应：', response)
            console.log('获取当前用户业务数据：', response.data)

            if (response.data.code === 200) {

                // 后端验证 Token 成功
                // 把用户信息重新保存到 Pinia
                console.log('Token验证成功，恢复用户信息')
                userInfo.value = response.data.data

                console.log('恢复后的userInfo：', userInfo.value)

            } else {
                console.log('Token无效')

                // Token 不合法或者已经失效
                userInfo.value = null

                // 同时删除浏览器中的旧 Token
                localStorage.removeItem('access_token')
            }

        } catch (error) {

            console.error('恢复登录状态失败：', error)
            // 请求失败时，也先清除当前登录状态
            userInfo.value = null
        }
    }

    // 退出登录
    const clearUserInfo = () => {
        userInfo.value = null
    }

    return {
        userInfo,
        isLogin,
        setUserInfo,
        initUser,
        clearUserInfo
    }
})