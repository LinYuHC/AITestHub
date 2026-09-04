<script setup lang="ts">
// 导入Vue相关函数
import { onMounted, ref } from 'vue'
// 导入接口调用方法
import { getPostsList, getPostDetail } from '../../api/blog/posts.ts'
// 导入数据类型定义
import type { PostListItem, PostDetail } from '../../types/posts.ts'
import { useUserStore } from '../../store/user.ts'
import {logout} from '../../api/user/user.ts'

const userStore = useUserStore()

console.log('当前用户：', userStore.userInfo)
console.log('是否登录：', userStore.isLogin)

// 定义响应式数据
const posts = ref<PostListItem[]>([])
const postsDateil = ref<PostDetail[]>([])
// 定义加载状态和错误信息
const loading = ref(false)
const errorMessage = ref('')

const searchTitle = ref('')
const currentPage = ref(1)
const pageSize = 3
const total = ref(0)

// 定义加载博客列表的方法
const loadPosts = async () => {
  loading.value = true
  errorMessage.value = ''

  try {
    const response = await getPostsList(
      // 获取搜索框的值
      searchTitle.value,
      // 获取当前页数
      currentPage.value,
      // 获取每页数量
      pageSize
    )
      // 获取当前页文章
    posts.value = response.data.data.items

    // 获取全部符合条件的数据量
    total.value = response.data.data.total

    console.log('后端完整响应：', response)
    console.log('后端业务数据：', response.data)
    console.log('博客数据：', response.data.data.items)
    console.log('总数量：', response.data.data.total)
    console.log('pageSize：', pageSize)

    posts.value = response.data.data.items
  } catch (error) {
    console.error('获取博客列表失败：', error)
    errorMessage.value = '获取博客列表失败'
  } finally {
    loading.value = false
  }
}
// 定义加载博客详情的方法
const loadPostDetail = async () => {
  loading.value = true
  errorMessage.value = ''

  try {
    const response1 = await getPostDetail(50)

    console.log('博客详情-后端完整响应：', response1)
    console.log('博客详情-后端业务数据：', response1.data)
    // console.log('博客数据：', response1.data.data.items)

    postsDateil.value = response1.data.data
  } catch (error) {
    console.error('获取博客详情失败：', error)
    errorMessage.value = '获取博客详情失败'
  } finally {
    loading.value = false
  }
}

// 分页
const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--
    loadPosts()
  }
}
const nextPage = () => {
  if (currentPage.value < Math.ceil(total.value / pageSize)) {
    currentPage.value++
    loadPosts()
  }
}

// 退出登录
const logout_user = async () => {
    try {
    // 调用退出登录接口
    const response = await logout()
    console.log('退出登录成功',response)
    // 清空localStorage中的Token
    localStorage.removeItem('access_token')
    // 清空用户信息
    useUserStore().clearUserInfo()
  } catch (error) {
    console.error('退出登录失败：', error)
    errorMessage.value = '退出登录失败'
  }



}

// 在组件挂载时加载博客列表
onMounted(() => {
  loadPosts()
  loadPostDetail()
  prevPage()
  nextPage()
})
</script>


<!--
  模板修改：
  - 为 <br> 添加 class="hide-br" 以便隐藏
  - 其余 class 名称与上次一致
-->
<template>
  <div class="blog-app">

    <div class="app-header">

      <h1 class="brand-title">
        &lt;AITestHub_Blog /&gt;
      </h1>

      <!-- v-if="!userStore.isLogin"表示：判断当前用户是否为登录状态，如果不是则显示登录按钮，反之显示头像-->
      <div class="nav-link login-link" v-if="!userStore.isLogin">
        <!-- login 链接 -->
        <router-link to="/login"  >login</router-link>
      </div>
      <div class="nav-link login-link" v-else>
        <button @click="logout_user" >logout</button>
        <!-- 用户头像 -->
        <img
            v-if="userStore.userInfo?.avatar"
            :src="userStore.userInfo.avatar"
            alt="用户头像"
            class="user-avatar"
        />

        <!-- 没有头像时显示默认头像 -->
        <div
            v-else
            class="default-avatar"
        >
            {{ userStore.userInfo?.nickname?.charAt(0).toUpperCase() }}
        </div>

        <!-- 用户名 -->
        <span class="username">
            {{ userStore.userInfo?.nickname || userStore.userInfo?.username }}
        </span>
      </div>



      <!-- 添加隐藏的换行 -->
      <br class="hide-br">
      <!-- blogCreate 链接 -->
      <router-link to="/blogCreate" class="nav-link create-link">blogCreate</router-link>

      <p class="terminal-line">
        <span class="terminal-prompt">&gt;</span>
        knowledge_is_power.exe
        <span class="terminal-cursor">_</span>
      </p>

    </div>

    <!-- 其余部分不变 -->
    <div class="search-section">
      <span class="shell-prefix">$</span>
      <input v-model="searchTitle" class="search-input" placeholder="search --title ...">
      <button class="search-btn" @click="loadPosts">搜索</button>
    </div>

    <p v-if="loading" class="loading-indicator"><span>&gt;</span> LOADING_DATA...</p>
    <p v-if="errorMessage" class="error-box"><span>[ERROR]</span> {{ errorMessage }}</p>

    <div class="posts-grid">
      <div v-for="post in posts" :key="post.id" class="post-card">
        <div class="card-header">
          <p class="post-id">ID:{{ post.id }}</p>
          <span class="status-badge">ONLINE</span>
        </div>
        <h2 class="post-title">{{ post.title }}</h2>
        <p class="post-summary">{{ post.summary }}</p>
        <div class="card-footer">
          <span class="views-count">阅读量:{{ post.views_count }}</span>
          <router-link class="detail-link" :to="`/blog/${post.id}`">[ 详情 ]</router-link>
        </div>
      </div>
    </div>

    <div class="pagination-bar">
      <button class="page-btn" @click="prevPage">&lt; PREV</button>
      <span class="page-info">PAGE <span class="page-current">{{ currentPage }}</span> / {{ Math.ceil(total / pageSize) }}</span>
      <button class="page-btn" @click="nextPage">NEXT &gt;</button>
    </div>

    <div class="app-footer">
      <span>&gt; AITestHub</span>
      <span>system.status: ONLINE</span>
    </div>

  </div>
</template>

<!--
  样式：对称布局，标题居中，左 blogCreate，右 login
  隐藏 <br>，使用 order 重排元素
-->
<style scoped>
/* =========================================================
 * 全局重置 & 基础
 * ========================================================= */
:global(body) {
  margin: 0;
  background: #f0f4f8;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  color: #1e293b;
  line-height: 1.6;
}
:global(*) {
  box-sizing: border-box;
}

/* =========================================================
 * 主容器
 * ========================================================= */
.blog-app {
  max-width: 1100px;
  margin: 32px auto;
  padding: 32px 36px 28px;
  background: #ffffff;
  border-radius: 28px;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.06);
}

/* =========================================================
 * 头部 – 使用 Flex + order 实现对称
 * ========================================================= */
.app-header {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between; /* 左右分散 */
  padding-bottom: 16px;
  border-bottom: 1px solid #e9edf2;
  margin-bottom: 28px;
  position: relative;
}

/* 隐藏原有的换行 */
.hide-br {
  display: none;
}

/* ----- 标题：居中 ----- */
.brand-title {
  font-size: 2.2rem;
  font-weight: 700;
  margin: 0;
  color: #0b2b4a;
  letter-spacing: -0.5px;
  order: 2;               /* 排在中间 */
  flex: 1;               /* 占据剩余空间，实现居中 */
  text-align: center;    /* 文字居中 */
}

/* ----- blogCreate 链接：左侧 ----- */
.create-link {
  order: 1;               /* 左侧 */
  margin-right: auto;    /* 靠左 */
}

/* ----- login 链接：右侧 ----- */
.login-link {
  order: 3;               /* 右侧 */
  margin-left: auto;     /* 靠右 */
}

/* 导航链接通用样式 */
.nav-link {
  text-decoration: none;
  font-weight: 500;
  font-size: 0.95rem;
  padding: 6px 18px;
  border-radius: 30px;
  transition: all 0.2s;
  display: inline-block;
}

.create-link {
  color: #2b7be4;
  background: rgba(43, 123, 228, 0.06);
  border: 1px solid rgba(43, 123, 228, 0.15);
}
.create-link:hover {
  background: #2b7be4;
  color: #fff;
  border-color: #2b7be4;
  box-shadow: 0 4px 12px rgba(43, 123, 228, 0.25);
}

.login-link {
  color: #1e293b;
  background: #f1f4f8;
  border: 1px solid #d0d7de;
}
.login-link:hover {
  background: #e2e8f0;
  border-color: #b0b8c0;
}

/* ----- 终端提示：换行，居中 ----- */
.terminal-line {
  order: 10;                  /* 放在最后 */
  flex-basis: 100%;          /* 占满一整行 */
  text-align: center;
  margin: 8px 0 0;
  font-size: 0.85rem;
  color: #6b7a8a;
  font-family: 'Fira Code', monospace;
}
.terminal-prompt {
  color: #20c997;
  margin-right: 4px;
}
.terminal-cursor {
  display: inline-block;
  width: 8px;
  height: 1.2em;
  background: #20c997;
  vertical-align: text-bottom;
  animation: blink 1s step-end infinite;
}
@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}

/* =========================================================
 * 搜索区域
 * ========================================================= */
.search-section {
  display: flex;
  align-items: center;
  gap: 10px;
  background: #f7f9fc;
  border: 1px solid #e2e8f0;
  border-radius: 60px;
  padding: 4px 4px 4px 20px;
  margin-bottom: 36px;
  transition: border-color 0.2s, box-shadow 0.2s;
}
.search-section:focus-within {
  border-color: #2b7be4;
  box-shadow: 0 0 0 4px rgba(43, 123, 228, 0.08);
}
.shell-prefix {
  color: #2b7be4;
  font-weight: 600;
  font-size: 1rem;
}
.search-input {
  flex: 1;
  border: none;
  background: transparent;
  padding: 12px 0;
  font-size: 0.95rem;
  outline: none;
  color: #1e293b;
}
.search-input::placeholder {
  color: #9aa9b9;
}
.search-btn {
  background: linear-gradient(135deg, #2b7be4, #1c6bc9);
  color: #fff;
  border: none;
  border-radius: 40px;
  padding: 10px 28px;
  font-weight: 600;
  font-size: 0.85rem;
  cursor: pointer;
  transition: all 0.25s;
  letter-spacing: 0.3px;
}
.search-btn:hover {
  transform: scale(1.02);
  box-shadow: 0 8px 20px rgba(43, 123, 228, 0.25);
}

/* =========================================================
 * 加载 & 错误
 * ========================================================= */
.loading-indicator {
  text-align: center;
  color: #2b7be4;
  font-size: 0.9rem;
  margin: 24px 0;
  opacity: 0.7;
}
.error-box {
  background: #fef2f2;
  border-left: 4px solid #f87171;
  padding: 12px 18px;
  border-radius: 8px;
  color: #b91c1c;
  font-size: 0.9rem;
  margin: 20px 0;
}
.error-box span {
  font-weight: 700;
  margin-right: 8px;
}

/* =========================================================
 * 文章卡片
 * ========================================================= */
.posts-grid {
  display: grid;
  gap: 24px;
  margin: 24px 0 32px;
}
.post-card {
  background: #ffffff;
  border: 1px solid #edf2f7;
  border-radius: 20px;
  padding: 24px 28px;
  transition: all 0.25s ease;
  box-shadow: 0 2px 6px rgba(0,0,0,0.02);
}
.post-card:hover {
  transform: translateY(-3px);
  border-color: #cbd5e1;
  box-shadow: 0 12px 28px rgba(0, 0, 0, 0.05);
}
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}
.post-id {
  font-size: 0.75rem;
  color: #8b9aa8;
  font-family: 'Fira Code', monospace;
  margin: 0;
}
.status-badge {
  font-size: 0.65rem;
  padding: 2px 12px;
  border-radius: 30px;
  background: #e6f7f0;
  color: #20c997;
  font-weight: 600;
  border: 1px solid #b8e6d9;
  letter-spacing: 0.4px;
}
.post-title {
  font-size: 1.6rem;
  font-weight: 600;
  margin: 0 0 10px;
  color: #0b2b4a;
}
.post-summary {
  color: #4b5a6a;
  font-size: 0.95rem;
  margin: 0 0 18px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 16px;
  border-top: 1px solid #edf2f7;
}
.views-count {
  color: #8b9aa8;
  font-size: 0.8rem;
  font-family: 'Fira Code', monospace;
}
.detail-link {
  background: transparent;
  border: 1px solid #2b7be4;
  border-radius: 40px;
  padding: 5px 18px;
  color: #2b7be4;
  text-decoration: none;
  font-size: 0.75rem;
  font-weight: 600;
  transition: all 0.2s;
}
.detail-link:hover {
  background: #2b7be4;
  color: #fff;
  box-shadow: 0 4px 12px rgba(43, 123, 228, 0.2);
}

/* =========================================================
 * 分页
 * ========================================================= */
.pagination-bar {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 18px;
  padding: 18px 0 6px;
  border-top: 1px solid #edf2f7;
}
.page-btn {
  background: transparent;
  border: 1px solid #d0d7de;
  border-radius: 40px;
  padding: 7px 22px;
  color: #1e293b;
  font-size: 0.8rem;
  cursor: pointer;
  transition: all 0.2s;
  font-weight: 500;
}
.page-btn:hover {
  border-color: #2b7be4;
  color: #2b7be4;
  background: #f7faff;
}
.page-info {
  color: #6b7a8a;
  font-size: 0.85rem;
}
.page-current {
  color: #2b7be4;
  font-weight: 700;
  margin: 0 4px;
}

/* =========================================================
 * 页脚
 * ========================================================= */
.app-footer {
  display: flex;
  justify-content: space-between;
  margin-top: 36px;
  padding-top: 18px;
  border-top: 1px solid #edf2f7;
  color: #8b9aa8;
  font-size: 0.75rem;
  letter-spacing: 0.3px;
}
.app-footer span:last-child {
  color: #20c997;
}

/* =========================================================
 * 响应式
 * ========================================================= */
@media (max-width: 640px) {
  .blog-app {
    margin: 16px;
    padding: 20px 18px;
    border-radius: 20px;
  }
  .brand-title {
    font-size: 1.8rem;
  }
  .app-header {
    flex-direction: column;
    align-items: stretch;
  }
  .brand-title {
    order: 0;
    flex: none;
    text-align: center;
  }
  .create-link {
    order: 1;
    margin: 6px 0 0;
    text-align: center;
  }
  .login-link {
    order: 2;
    margin: 6px 0 0;
    text-align: center;
  }
  .terminal-line {
    order: 3;
  }
  .search-section {
    padding: 4px 4px 4px 14px;
  }
  .search-btn {
    padding: 8px 16px;
    font-size: 0.75rem;
  }
  .post-card {
    padding: 18px;
  }
  .post-title {
    font-size: 1.3rem;
  }
  .pagination-bar {
    flex-wrap: wrap;
    gap: 10px;
  }
  .app-footer {
    flex-direction: column;
    align-items: flex-start;
    gap: 4px;
  }
}
</style>