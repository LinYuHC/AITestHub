<script setup lang="ts">
import {ref} from 'vue'
// 导入模型
import type {CreatePostRequest} from '../../types/posts.ts'
// 导入接口
import {createPost} from '../../api/blog/posts.ts'


  const createPostData : CreatePostRequest = {
  title: '',
  summary: '',
  content: '',
  status: 2,
  category_id: 1,
  cover_image: '',
  allow_comment: true,
  is_top: false
}

const create_Post = async () => {

  // 调用创建博客接口
  const response = await createPost(createPostData)
  console.log('创建博客响应===',response)
}

</script>

<!--
  模板修改：
  - 为根 div 添加 class="create-post-page"
  - 为标题 h1 添加 class="page-heading"
  - 为表单添加 class="post-form"
  - 每个表单项包裹 div 添加 class="form-group"
  - 为 label 添加 class="form-label"
  - 为 input/textarea 添加 class="form-input" 或 "form-textarea"
  - 为复选框包裹 div 添加 class="checkbox-group"
  - 为提交按钮添加 class="submit-btn"
  未改动任何业务逻辑或数据绑定。
-->
<template>
  <div class="create-post-page">
    <h1 class="page-heading">✨ 创建新博客</h1>

    <form @submit.prevent="create_Post" class="post-form">
      <!-- 标题 -->
      <div class="form-group">
        <label for="title" class="form-label">标题</label>
        <input type="text" id="title" v-model="createPostData.title" required class="form-input" placeholder="输入文章标题...">
      </div>

      <!-- 摘要 -->
      <div class="form-group">
        <label for="summary" class="form-label">摘要</label>
        <input type="text" id="summary" v-model="createPostData.summary" required class="form-input" placeholder="简短描述文章内容...">
      </div>

      <!-- 正文（支持 HTML） -->
      <div class="form-group">
        <label for="content" class="form-label">正文（支持 HTML 标签）</label>
        <textarea id="content" v-model="createPostData.content" required class="form-textarea" placeholder="可直接粘贴带 HTML 的笔记源码，如 &lt;h1&gt;标题&lt;/h1&gt;&lt;p&gt;段落...&lt;/p&gt;"></textarea>
        <span class="hint">💡 支持所有 HTML 标签，详情页将自动渲染样式</span>
      </div>

      <!-- 分类 ID -->
      <div class="form-group">
        <label for="category_id" class="form-label">分类 ID</label>
        <input type="number" id="category_id" v-model="createPostData.category_id" required class="form-input" placeholder="输入分类编号">
      </div>

      <!-- 封面图 URL -->
      <div class="form-group">
        <label for="cover_image" class="form-label">封面图 URL</label>
        <input type="text" id="cover_image" v-model="createPostData.cover_image" required class="form-input" placeholder="https://example.com/cover.jpg">
      </div>

      <!-- 复选框区域（允许评论 & 置顶） -->
      <div class="checkbox-row">
        <div class="checkbox-group">
          <input type="checkbox" id="allow_comment" v-model="createPostData.allow_comment">
          <label for="allow_comment" class="checkbox-label">允许评论</label>
        </div>
        <div class="checkbox-group">
          <input type="checkbox" id="is_top" v-model="createPostData.is_top">
          <label for="is_top" class="checkbox-label">置顶文章</label>
        </div>
      </div>

      <button type="submit" class="submit-btn">🚀 发布文章</button>
    </form>
  </div>
</template>

<style scoped>
/* =========================================================
 * 全局重置（与列表/详情页一致）
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
 * 创建页面容器 – 居中卡片，大气留白
 * ========================================================= */
.create-post-page {
  max-width: 820px;
  margin: 40px auto;
  padding: 48px 56px;
  background: #ffffff;
  border-radius: 28px;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.06);
  transition: box-shadow 0.2s;
}

/* =========================================================
 * 页面标题
 * ========================================================= */
.page-heading {
  font-size: 2.4rem;
  font-weight: 700;
  margin: 0 0 32px 0;
  color: #0b2b4a;
  letter-spacing: -0.3px;
  text-align: center;
}

/* =========================================================
 * 表单
 * ========================================================= */
.post-form {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

/* ----- 每个字段组 ----- */
.form-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.form-label {
  font-weight: 600;
  font-size: 0.95rem;
  color: #1e293b;
  letter-spacing: 0.2px;
}

/* 通用输入框 */
.form-input,
.form-textarea {
  width: 100%;
  padding: 12px 16px;
  border: 1px solid #d0d7de;
  border-radius: 12px;
  font-size: 0.95rem;
  font-family: inherit;
  background: #fafcff;
  transition: border-color 0.2s, box-shadow 0.2s;
  outline: none;
  color: #1e293b;
}
.form-input:focus,
.form-textarea:focus {
  border-color: #2b7be4;
  box-shadow: 0 0 0 4px rgba(43, 123, 228, 0.08);
}
.form-input::placeholder,
.form-textarea::placeholder {
  color: #9aa9b9;
}

/* 文本域 */
.form-textarea {
  min-height: 200px;
  resize: vertical;
  line-height: 1.7;
}

/* 提示文字 */
.hint {
  font-size: 0.8rem;
  color: #6b7a8a;
  margin-top: 4px;
  display: flex;
  align-items: center;
  gap: 4px;
}

/* ----- 复选框行（水平排列）----- */
.checkbox-row {
  display: flex;
  gap: 32px;
  align-items: center;
  padding: 8px 0;
}

.checkbox-group {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
}
.checkbox-group input[type="checkbox"] {
  width: 18px;
  height: 18px;
  accent-color: #2b7be4;
  cursor: pointer;
}
.checkbox-label {
  font-weight: 500;
  font-size: 0.95rem;
  color: #1e293b;
  cursor: pointer;
}

/* ----- 提交按钮 ----- */
.submit-btn {
  background: linear-gradient(135deg, #2b7be4, #1c6bc9);
  color: #fff;
  border: none;
  border-radius: 60px;
  padding: 16px 36px;
  font-size: 1.1rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.25s;
  margin-top: 12px;
  letter-spacing: 0.5px;
  box-shadow: 0 4px 12px rgba(43, 123, 228, 0.2);
}
.submit-btn:hover {
  transform: scale(1.02);
  box-shadow: 0 8px 24px rgba(43, 123, 228, 0.3);
}
.submit-btn:active {
  transform: scale(0.98);
}

/* =========================================================
 * 响应式
 * ========================================================= */
@media (max-width: 640px) {
  .create-post-page {
    margin: 20px 16px;
    padding: 28px 20px;
    border-radius: 20px;
  }
  .page-heading {
    font-size: 1.8rem;
  }
  .checkbox-row {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }
  .submit-btn {
    padding: 14px 24px;
    font-size: 1rem;
  }
}
</style>