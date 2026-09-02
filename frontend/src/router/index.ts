// 从 vue-router 导入创建路由和创建 history 的方法
import { createRouter, createWebHistory } from 'vue-router'

// 导入博客列表页面
import BlogList from '../views/blog/BlogList.vue'

// 导入博客详情页面
import BlogDetail from '../views/blog/BlogDetail.vue'
// 导入登录页面
import Login from '../views/user/login.vue'
// 导入创建blog页面
import BlogCreate from '../views/blog/BlogCreate.vue'
// 导入Markdown编辑器组件
import MarkdownEditor from '../components/MarkdownEditor.vue'
// 导入封面图上传组件
import CoverImageUploader from '../components/CoverImageUploader.vue'


// 创建 Router 实例
const router = createRouter({

  // createWebHistory 表示使用浏览器正常的 URL 形式
  // 例如：
  // http://localhost:5173/blog
  // 而不是：
  // http://localhost:5173/#/blog
  history: createWebHistory(),

  // 路由规则
  routes: [

    // -----------------------------
    // 博客列表
    // URL：
    // /blog
    // -----------------------------
    {
      path: '/blog',
      name: 'BlogList',
      component: BlogList
    },

    // -----------------------------
    // 博客详情
    //
    // :id 是动态参数
    //
    // 当访问：
    // /blog/1
    //
    // 那么：
    // id = 1
    //
    // 当访问：
    // /blog/20
    //
    // 那么：
    // id = 20
    // -----------------------------
    {
      path: '/blog/:id',
      name: 'BlogDetail',
      component: BlogDetail
    },

    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/blogCreate',
      name: 'BlogCreate',
      component: BlogCreate
    },
    {
      path: '/MarkdownEditor',
      name: 'MarkdownEditor',
      component: MarkdownEditor
    },
    {
      path: '/CoverImageUploader',
      name: 'CoverImageUploader',
      component: CoverImageUploader
    }

  ]
})


// 把 router 导出去
// main.ts 会使用它
export default router