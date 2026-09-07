<script setup lang="ts">
// ref：创建响应式数据
// onMounted：页面加载完成后执行代码
import { ref, onMounted } from 'vue'

// useRoute：获取当前路由信息
import { useRoute } from 'vue-router'

// 导入接口调用
import { getPostDetail } from '../../api/blog/posts.ts'

// 导入文章详情类型
import type { PostDetail } from '../../types/posts.ts'

// 导入 md-editor-v3 的纯预览组件
// 详情页不再使用 marked，而是直接使用 MdPreview
import { MdPreview } from 'md-editor-v3'

// 导入 MdPreview 的样式
import 'md-editor-v3/lib/preview.css'

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

// ------------------------------------
// MdPreview 的组件 ID
//
// md-editor-v3 的预览组件需要一个 id。
// 使用固定值即可。
// ------------------------------------
const previewId = 'blog-detail-preview'

// 请求文章详情
const loadPostDateil = async () => {

  // 从 URL 中获取 id，注意：Vue Router 的 params 默认是 string，例如：route.params.id = "2"，但我们的后端方法需要 number，所以要进行 Number 转换。
  const id = Number(route.params.id)

  // 调用获取文章详情的方法
  const response = await getPostDetail(id)

  // ------------------------------------
  // 判断后端业务响应是否成功
  // ------------------------------------
  if (response.data.code === 200) {

    // 把后端返回的数据保存到响应式变量
    post.value = response.data.data

    console.log('文章详情：', response.data.data)

  } else {

    console.error(
      '获取文章详情失败：',
      response.data.message
    )
  }
}

// 页面挂载完成以后请求文章详情
onMounted(() => {
  loadPostDateil()
})
</script>

<!--
  模板修改：
  - 为根 div 增加 class="post-detail-page"
  - 加载状态增加 class="loading-state"
  - 文章内容容器增加 class="post-content-wrapper"
  - 标题、摘要、封面分别增加 class
  - 原来的 v-html + marked 已经移除
  - 文章正文改成 MdPreview
  - MdPreview 直接读取数据库中的 Markdown 原文
  - 返回博客列表地址从 "/" 修改为 "/blog"

  未改动文章请求逻辑。
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
      <img
        v-if="post.cover_image"
        :src="post.cover_image"
        alt="封面图"
        class="post-cover"
      />

      <!-- 文章标题 -->
      <h1 class="post-title">
        {{ post.title }}
      </h1>

      <!-- 文章摘要（可选） -->
      <div
        v-if="post.summary"
        class="post-summary-block"
      >
        {{ post.summary }}
      </div>

      <!--
        Markdown 正文

        不再使用：

        marked
        + v-html
        + mermaid

        而是直接使用 md-editor-v3 自己提供的 MdPreview。

        这样创建文章页面的预览和详情页
        使用的是同一套 Markdown 渲染机制。
      -->
      <div class="post-body">
        <MdPreview
          :id="previewId"
          :modelValue="post.content"
        />
      </div>

      <!-- 返回博客列表 -->
      <router-link
        to="/blog"
        class="back-link"
      >
        ← 返回博客列表
      </router-link>

    </div>
  </div>
</template>

<style scoped>

/* =========================================================
 * 全局重置 & 字体
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
 * 详情页容器
 * ========================================================= */
.post-detail-page {
  max-width: 900px;
  margin: 40px auto;
  padding: 40px 48px;
  background: #ffffff;
  border-radius: 28px;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.06);
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
 * 摘要
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
 * Markdown 正文容器
 * ========================================================= */
.post-body {
  margin-top: 20px;
  width: 100%;
}

/* =========================================================
 * MdPreview
 * =========================================================
 *
 * 不重新定义 Markdown 的整体样式，
 * 主要使用 md-editor-v3 自己的默认样式。
 * ========================================================= */

.post-body :deep(.md-editor-preview) {
  width: 100%;
  max-width: 100%;
}

/* =========================================================
 * 解决代码块内容居中问题
 * =========================================================
 *
 * 强制代码块：
 * 1. 整个代码区域左对齐
 * 2. pre 左对齐
 * 3. code 左对齐
 * 4. 代码内部内容左对齐
 *
 * !important 是为了覆盖 md-editor-v3
 * 或其他全局样式造成的 text-align。
 * ========================================================= */

.post-body :deep(.md-editor-preview pre) {
  text-align: left !important;
}

.post-body :deep(.md-editor-preview pre code) {
  display: block;
  width: 100%;
  text-align: left !important;
}

/* =========================================================
 * md-editor-v3 代码块内部
 * =========================================================
 *
 * md-editor-v3 某些版本的代码块会增加额外容器，
 * 所以继续把常见的代码相关容器统一设置为左对齐。
 * ========================================================= */

.post-body :deep(.md-editor-preview .md-editor-code-block) {
  text-align: left !important;
}

.post-body :deep(.md-editor-preview .md-editor-code-block pre) {
  text-align: left !important;
}

.post-body :deep(.md-editor-preview .md-editor-code-block code) {
  text-align: left !important;
}

/* =========================================================
 * 代码行
 * =========================================================
 *
 * 如果代码高亮插件给每一行增加 span，
 * 同样强制左对齐。
 * ========================================================= */

.post-body :deep(.md-editor-preview pre span) {
  text-align: left !important;
}

/* =========================================================
 * Mermaid
 * =========================================================
 *
 * Mermaid 图表需要保持居中，
 * 所以这里单独让 Mermaid 居中。
 * ========================================================= */

.post-body :deep(.md-editor-preview .mermaid) {
  width: 100%;
  max-width: 100%;
  overflow-x: auto;
  text-align: center !important;
}

/* Mermaid SVG */
.post-body :deep(.md-editor-preview .mermaid svg) {
  max-width: 100%;
  height: auto;
}

/* =========================================================
 * 正文图片
 * ========================================================= */
.post-body :deep(.md-editor-preview img) {
  max-width: 100%;
  height: auto;
}

/* =========================================================
 * 防止超长代码撑破页面
 * ========================================================= */

.post-body :deep(.md-editor-preview pre) {
  max-width: 100%;
  overflow-x: auto;
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