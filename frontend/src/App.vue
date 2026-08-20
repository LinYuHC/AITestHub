<script setup lang="ts">
interface PostItem {
  id: number
  title: string
  summary: string
  category: string
  viewsCount: number
  createdAt: string
}

const posts1: PostItem[] = [
  {
    id: 1,
    title: 'FastAPI 博客后端开发记录',
    summary: '记录 OpenHub 博客系统的接口设计、认证和数据库分层。',
    category: 'FastAPI',
    viewsCount: 128,
    createdAt: '2026-08-20',
  },
  {
    id: 2,
    title: 'Vue 3 前端项目初始化',
    summary: '从 Vite + Vue + TypeScript 开始搭建博客前端。',
    category: 'Vue',
    viewsCount: 76,
    createdAt: '2026-08-20',
  },
]
</script>
<template>
  <main class="page">
    <h1>OpenHub Blog</h1>

    <section class="post-list">
      <article v-for="post in posts1" :key="post.id" class="post-card">
        <h2>{{ post.title }}</h2>
        <p>{{ post.summary }}</p>

        <div class="meta">
          <span>{{ post.category }}</span>
          <span>阅读 {{ post.viewsCount }}</span>
          <span>{{ post.createdAt }}</span>
        </div>
      </article>
    </section>
  </main>
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