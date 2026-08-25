<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { getPostsList } from '../api/posts'
import type { PostListItem } from '../types/post'

const posts = ref<PostListItem[]>([])
const loading = ref(false)
const errorMessage = ref('')

const loadPosts = async () => {
  loading.value = true
  errorMessage.value = ''

  try {
    const response = await getPostsList()

    console.log('后端完整响应：', response)
    console.log('后端业务数据：', response.data)
    console.log('博客数据：', response.data.data.items)

    posts.value = response.data.data.items
  } catch (error) {
    console.error('获取博客列表失败：', error)
    errorMessage.value = '获取博客列表失败'
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadPosts()
})
</script>
<template>
  <div class="blog-list">
    <h1>AITestHub Blog</h1>
    <p v-if="loading">
      正在加载...
    </p>
    <p v-if="errorMessage">
      {{ errorMessage }}
    </p>
    <div
      v-for="post in posts"
      :key="post.id"
      class="post-item"
    >
      <h2>{{ post.title }}</h2>
      <p>{{ post.summary }}</p>
      <span>
        阅读量：{{ post.views_count }}
      </span>
    </div>
  </div>
</template>
<style scoped>
.blog-list {
  width: 800px;
  margin: 0 auto;
}

.post-item {
  padding: 20px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
}
</style>
