import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

// 导入Router
import router from "./router";

// 创建Vue应用
const app = createApp(App)

// 注册 Vue Router,注册之后，所有页面都可以使用路由功能
app.use(router)

// 挂载Vue应用
app.mount('#app')
