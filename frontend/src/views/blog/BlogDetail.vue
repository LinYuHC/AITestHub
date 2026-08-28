<script setup lang="ts">
// ref：创建响应式数据
// onMounted：页面加载完成后执行代码
import { ref, onMounted, computed} from 'vue'
// useRoute：获取当前路由信息
import { useRoute } from  'vue-router'
// 导入接口调用
import { getPostDetail } from '../../api/blog/posts.ts'
// 导入文章详情类型
import type{ PostDetail } from '../../types/posts.ts'
import { marked } from 'marked'
// ...
const renderedContent = computed(() => {
  return post.value ? marked(post.value.content) : ''
})

// ------------------------------------
// 获取当前路由对象
// ------------------------------------
//
// 如果当前地址是：
// /blog/2
//
// 那么 route.params.id 就是：
// "2"
// ------------------------------------
const route = useRoute()

// ------------------------------------
// 定义文章详情数据
//
// 页面刚打开的时候还没有文章数据
// 所以先使用 null
// ------------------------------------
const post = ref<PostDetail | null>(null)

// 请求文章详情
const loadPostDateil = async () => {
  // 从 URL 中获取 id
  //注意：Vue Router 的 params 默认是 string,即：route.params.id = "2",但我们的后端方法需要：number,所以要进行 Number 转换。
  const id = Number(route.params.id)

  //   调用获取文章详情的方法
  const response = await getPostDetail(id)
  // 把后端返回的数据保存到响应式变量
  post.value = response.data.data
  console.log('文章详情：', response.data.data)

}
// 页面挂载完成以后请求文章详情
  onMounted(()=>{
    loadPostDateil()
  })
</script>

<!--
  模板修改：
  - 为根 div 增加 class="post-detail-page"
  - 加载状态增加 class="loading-state"
  - 文章内容容器增加 class="post-content-wrapper"
  - 标题、摘要、内容、封面分别增加 class
  - 内容使用 v-html 渲染，并包裹在 class="post-body" 中
  未改动任何逻辑或注释。
-->
<template>
  <div class="post-detail-page">
    <!-- 加载状态 -->
    <p v-if="!post" class="loading-state">
      <span>&gt;</span> 正在加载文章...
    </p>

    <!-- 文章详情 -->
    <div v-else class="post-content-wrapper">
      <!-- 封面图（如果有） -->
      <img v-if="post.cover_image" :src="post.cover_image" alt="封面图" class="post-cover" />

      <!-- 文章标题 -->
      <h1 class="post-title">{{ post.title }}</h1>

      <!-- 文章摘要（可选） -->
      <div v-if="post.summary" class="post-summary-block">
        {{ post.summary }}
      </div>

      <!-- 文章正文（使用 v-html 自动排版） -->
      <div class="post-body" v-html="renderedContent"></div>

      <!-- 返回链接（可选，提升用户体验） -->
      <router-link to="/" class="back-link">← 返回博客列表</router-link>
    </div>
  </div>
</template>

<style scoped>
/* =========================================================
 * 全局重置 & 字体（与列表页一致）
 * ========================================================= */
:global(body) {
  margin: 0;
  background: #f0f4f8;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  color: #1e293b;
  line-height: 1.7;
}
:global(*) {
  box-sizing: border-box;
}

/* =========================================================
 * 详情页容器 – 居中卡片
 * ========================================================= */
.post-detail-page {
  max-width: 900px;
  margin: 40px auto;
  padding: 40px 48px;
  background: #ffffff;
  border-radius: 28px;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.06);
  transition: box-shadow 0.2s;
}

/* =========================================================
 * 加载状态
 * ========================================================= */
.loading-state {
  text-align: center;
  font-size: 1.1rem;
  color: #2b7be4;
  opacity: 0.8;
  margin: 60px 0;
}
.loading-state span {
  color: #20c997;
  margin-right: 8px;
}

/* =========================================================
 * 封面图
 * ========================================================= */
.post-cover {
  width: 100%;
  max-height: 420px;
  object-fit: cover;
  border-radius: 16px;
  margin-bottom: 28px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
}

/* =========================================================
 * 文章标题
 * ========================================================= */
.post-title {
  font-size: 2.8rem;
  font-weight: 700;
  margin: 0 0 16px 0;
  color: #0b2b4a;
  line-height: 1.2;
  letter-spacing: -0.3px;
}

/* =========================================================
 * 摘要块
 * ========================================================= */
.post-summary-block {
  background: #f7faff;
  border-left: 4px solid #2b7be4;
  padding: 16px 22px;
  margin: 12px 0 28px 0;
  border-radius: 8px;
  color: #2c3e50;
  font-size: 1.1rem;
  font-weight: 500;
  font-style: italic;
}

/* =========================================================
 * 正文 – 自动排版（对 v-html 生成的内容）
 * ========================================================= */
.post-body {
  font-size: 1.05rem;
  color: #1e293b;
}

/* 段落 */
.post-body p {
  margin: 1.2em 0;
}

/* 标题层级 */
.post-body h1,
.post-body h2,
.post-body h3,
.post-body h4,
.post-body h5,
.post-body h6 {
  margin: 1.8em 0 0.6em;
  font-weight: 600;
  line-height: 1.3;
  color: #0b2b4a;
}
.post-body h1 { font-size: 2rem; }
.post-body h2 { font-size: 1.7rem; border-bottom: 1px solid #e9edf2; padding-bottom: 0.3em; }
.post-body h3 { font-size: 1.4rem; }
.post-body h4 { font-size: 1.2rem; }

/* 列表 */
.post-body ul,
.post-body ol {
  padding-left: 1.8em;
  margin: 1em 0;
}
.post-body li {
  margin: 0.4em 0;
}

/* 代码块（行内与块级） */
.post-body code {
  font-family: 'Fira Code', 'JetBrains Mono', monospace;
  background: #f1f4f8;
  padding: 0.2em 0.6em;
  border-radius: 6px;
  font-size: 0.9em;
  color: #d63384;
}
.post-body pre {
  background: #1e293b;
  color: #e2e8f0;
  padding: 20px 24px;
  border-radius: 12px;
  overflow-x: auto;
  margin: 1.5em 0;
  font-family: 'Fira Code', monospace;
  font-size: 0.95rem;
  line-height: 1.6;
}
.post-body pre code {
  background: transparent;
  padding: 0;
  color: inherit;
  font-size: inherit;
}

/* 引用块 */
.post-body blockquote {
  margin: 1.5em 0;
  padding: 0.8em 1.5em;
  border-left: 4px solid #20c997;
  background: #f7fafc;
  border-radius: 0 8px 8px 0;
  color: #2d4055;
  font-style: italic;
}

/* 图片（正文中的） */
.post-body img {
  max-width: 100%;
  height: auto;
  border-radius: 12px;
  margin: 1.2em 0;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
}

/* 表格 */
.post-body table {
  width: 100%;
  border-collapse: collapse;
  margin: 1.5em 0;
}
.post-body th,
.post-body td {
  padding: 10px 14px;
  border: 1px solid #e2e8f0;
  text-align: left;
}
.post-body th {
  background: #f7fafc;
  font-weight: 600;
}

/* 分割线 */
.post-body hr {
  border: none;
  height: 1px;
  background: linear-gradient(to right, #e2e8f0, transparent);
  margin: 2em 0;
}

/* =========================================================
 * 返回链接
 * ========================================================= */
.back-link {
  display: inline-block;
  margin-top: 40px;
  color: #2b7be4;
  text-decoration: none;
  font-weight: 500;
  font-size: 0.95rem;
  padding: 8px 20px;
  border: 1px solid #d0d7de;
  border-radius: 40px;
  transition: all 0.2s;
}
.back-link:hover {
  background: #2b7be4;
  color: #fff;
  border-color: #2b7be4;
  box-shadow: 0 4px 12px rgba(43, 123, 228, 0.2);
}

/* =========================================================
 * 响应式
 * ========================================================= */
@media (max-width: 640px) {
  .post-detail-page {
    margin: 20px 16px;
    padding: 24px 20px;
    border-radius: 20px;
  }
  .post-title {
    font-size: 2rem;
  }
  .post-body {
    font-size: 0.95rem;
  }
  .post-summary-block {
    font-size: 1rem;
    padding: 12px 16px;
  }
}
</style>