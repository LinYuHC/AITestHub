import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
// 创建整个项目的“全局状态管理器”
import {createPinia} from "pinia";
// 导入用户 Store
import { useUserStore } from './store/user'
// 导入Router
import router from "./router";

// 创建Vue应用
const app = createApp(App)

// 注册 Vue Router,注册之后，所有页面都可以使用路由功能
app.use(router)

// 创建 Pinia
const pinia = createPinia()
// 注册 Pinia，Vue 项目里的组件都可以使用 Store
app.use(pinia)

// 获取用户 Store
const userStore = useUserStore(pinia)
// 应用启动时恢复登录状态
await userStore.initUser()

// 挂载Vue应用
app.mount('#app')
