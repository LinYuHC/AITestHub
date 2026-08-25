<script setup lang="ts">
// import type {PostListItem} from './types/post'
import BlogList from './views/BlogList.vue'

// const posts1: PostListItem[] = [
//   {
//     id: 1,
//     title: 'FastAPI 博客后端开发记录',
//     summary: '记录 OpenHub 博客系统的接口设计、认证和数据库分层。',
//     category: 'FastAPI',
//     views_count: 128,
//     author_id: 1,
//   },
//   {
//     id: 2,
//     title: 'Vue 3 前端项目初始化',
//     summary: '从 Vite + Vue + TypeScript 开始搭建博客前端。',
//     category: 'Vue',
//     views_count: 76,
//     author_id: 1,
//   },
// ]
</script>
<template>
   <BlogList />
<!--  <main class="page">-->
<!--    <h1>OpenHub Blog</h1>-->

<!--    <section class="post-list">-->
<!--      <article v-for="post in posts1" :key="post.id" class="post-card">-->
<!--        <h2>{{ post.title }}</h2>-->
<!--        <p>摘要: {{ post.summary }}</p>-->

<!--        <div class="meta">-->
<!--          <span>类别: {{ post.category }}</span>-->
<!--          <span>阅读: {{ post.views_count }}</span>-->
<!--&lt;!&ndash;          <span>{{ post.createdAt }}</span>&ndash;&gt;-->
<!--        </div>-->
<!--      </article>-->
<!--    </section>-->
<!--  </main>-->
</template>

<style scoped>
.page {
  max-width: 960px;
  margin: 0 auto;
  padding: 40px 24px;
}

.post-list {
  display: grid;
  gap: 16px;
}

.post-card {
  padding: 20px;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
}

.post-card h2 {
  margin: 0 0 8px;
}

.post-card p {
  color: #4b5563;
}

.meta {
  display: flex;
  gap: 16px;
  color: #6b7280;
  font-size: 14px;
}
</style>