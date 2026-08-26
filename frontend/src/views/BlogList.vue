<script setup lang="ts">
// 导入Vue相关函数
import { onMounted, ref } from 'vue'
// 导入接口调用方法
import { getPostsList, getPostDetail } from '../api/posts'
// 导入数据类型定义
import type { PostListItem, PostDetail } from '../types/posts.ts'

// 定义响应式数据
const posts = ref<PostListItem[]>([])
const postsDateil = ref<PostDetail[]>([])
// 定义加载状态和错误信息
const loading = ref(false)
const errorMessage = ref('')

// 定义加载博客列表的方法
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

// 在组件挂载时加载博客列表
onMounted(() => {
  loadPosts()
  loadPostDetail()
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
      <p>{{post.id}}</p>
      <h2>{{ post.title }}</h2>
      <p>{{ post.summary }}</p>
      <span>
        阅读量：{{ post.views_count }}
      </span>
      <!--
        点击后跳转：
        /blog/1
        /blog/2
        /blog/3
        :to 前面的冒号表示：
        这里不是普通字符串，
        而是一个 Vue 表达式。
      -->
      <router-link :to="`/blog/${post.id}`">详情</router-link>
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
