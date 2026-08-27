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

// 在组件挂载时加载博客列表
onMounted(() => {
  loadPosts()
  loadPostDetail()
  prevPage()
  nextPage()
})
</script>
<template>
  <!--
    博客页面最外层容器
    整个页面使用 cyber-blog 作为主题根节点，
    后面的 CSS 都以它为基础。
  -->
  <div class="cyber-blog">

    <!-- =========================
         页面头部
         ========================= -->
    <div class="blog-header">

      <!-- 页面标题 -->
      <h1 class="page-title">
        &lt;AITestHub_Blog /&gt;
      </h1>

      <!--
        类似终端中的提示符，
        增加黑客 / Terminal 氛围。
      -->
      <p class="terminal-tip">
        <span class="terminal-prefix">&gt;</span>
        knowledge_is_power.exe
        <span class="terminal-cursor">_</span>
      </p>

    </div>


    <!-- =========================
         搜索区域
         ========================= -->
    <div class="search-bar">

      <!--
        输入框前增加 $，
        模拟 Linux / Terminal 命令行。
      -->
      <span class="command-prefix">
        $
      </span>

      <!--
        你的原 input 标签保留，
        这里只增加 class 和 placeholder。
      -->
      <input
        v-model="searchTitle"
        class="search-input"
        placeholder="search --title ..."
      >

      <!--
        搜索按钮保留原 button 标签。
      -->
      <button
        class="search-button"
        @click="loadPosts"
      >
        EXECUTE
      </button>

    </div>


    <!-- =========================
         加载状态
         ========================= -->
    <p
      v-if="loading"
      class="loading-message"
    >
      <span>&gt;</span>
      LOADING_DATA...
    </p>


    <!-- =========================
         错误提示
         ========================= -->
    <p
      v-if="errorMessage"
      class="error-message"
    >
      <span>[ERROR]</span>
      {{ errorMessage }}
    </p>


    <!-- =========================
         博客列表
         ========================= -->
    <div class="post-list">

      <!--
        保留你原来的 v-for，
        只是增加 post-item class。
      -->
      <div
        v-for="post in posts"
        :key="post.id"
        class="post-item"
      >

        <!--
          文章顶部信息。
          使用类似终端文件信息的感觉。
        -->
        <div class="post-header">

          <!-- 文章 ID -->
          <p class="post-id">
            ID://{{ post.id }}
          </p>

          <!--
            文章状态装饰。
            这里不需要新增数据，仅仅作为视觉元素。
          -->
          <span class="post-status">
            ONLINE
          </span>

        </div>


        <!-- 文章标题 -->
        <h2 class="post-title">
          {{ post.title }}
        </h2>


        <!--
          文章摘要。
        -->
        <p class="post-summary">
          {{ post.summary }}
        </p>


        <!-- =========================
             文章底部信息
             ========================= -->
        <div class="post-meta">

          <!-- 阅读量 -->
          <span class="post-views">
            VIEWS://{{ post.views_count }}
          </span>


          <!--
            router-link 保留，
            只增加 class。
          -->
          <router-link
            class="detail-link"
            :to="`/blog/${post.id}`"
          >
            [ ACCESS ]
          </router-link>

        </div>

      </div>

    </div>


    <!-- =========================
         分页
         ========================= -->
    <div class="pagination">

      <!-- 上一页 -->
      <button
        class="pagination-button"
        @click="prevPage"
      >
        &lt; PREV
      </button>


      <!-- 当前页信息 -->
      <span class="pagination-info">
        PAGE
        <span class="pagination-current">
          {{ currentPage }}
        </span>

        /
        {{ Math.ceil(total / pageSize) }}
      </span>


      <!-- 下一页 -->
      <button
        class="pagination-button"
        @click="nextPage"
      >
        NEXT &gt;
      </button>

    </div>


    <!-- =========================
         页面底部
         ========================= -->
    <div class="blog-footer">
      <span>&gt; AITestHub</span>
      <span>system.status: ONLINE</span>
    </div>

  </div>
</template>
<style scoped>

/* =========================================================
 * Cyber Blog 全局主题
 * =========================================================
 *
 * 页面整体视觉方向：
 *
 * 深黑背景
 * 荧光绿色为主色
 * 青色为辅助色
 * 等宽字体
 * 终端 / Hacker / Cyberpunk
 *
 * ========================================================= */


/* =========================================================
 * 1. 全局页面基础
 * ========================================================= */

/*
 * :global(body)
 *
 * 因为 <style scoped> 默认只作用于当前组件，
 * 所以 body 必须使用 :global 才能修改整个页面背景。
 */
:global(body) {
  margin: 0;

  /*
   * 使用深黑背景，
   * 比纯黑稍微亮一点，避免视觉过于生硬。
   */
  background: #05070a;

  /*
   * 等宽字体非常适合技术博客和 Terminal 风格。
   */
  font-family:
    "JetBrains Mono",
    "Cascadia Code",
    "Consolas",
    monospace;

  color: #d8f3dc;
}


/*
 * 全局页面盒模型统一。
 */
:global(*) {
  box-sizing: border-box;
}


/* =========================================================
 * 2. 页面整体容器
 * ========================================================= */

.cyber-blog {
  /*
   * 限制最大宽度，
   * 防止超宽显示器上内容铺得太开。
   */
  width: 100%;
  max-width: 1000px;

  margin: 0 auto;

  padding: 60px 24px 40px;

  /*
   * 页面使用相对定位，
   * 方便后面增加背景装饰。
   */
  position: relative;
}


/*
 * Cyber Grid：
 *
 * 使用两个 linear-gradient
 * 创建非常淡的网格背景。
 *
 * 这样不会真的增加 DOM，
 * 纯 CSS 就能产生 Cyberpunk 背景。
 */
.cyber-blog::before {
  content: "";

  position: fixed;

  inset: 0;

  pointer-events: none;

  background-image:
    linear-gradient(
      rgba(0, 255, 136, 0.025) 1px,
      transparent 1px
    ),
    linear-gradient(
      90deg,
      rgba(0, 255, 136, 0.025) 1px,
      transparent 1px
    );

  background-size: 30px 30px;

  /*
   * 保证背景在内容下面。
   */
  z-index: -2;
}


/*
 * 添加一层非常淡的绿色光晕，
 * 增加黑客终端氛围。
 */
.cyber-blog::after {
  content: "";

  position: fixed;

  top: -200px;
  left: 50%;

  width: 500px;
  height: 500px;

  transform: translateX(-50%);

  pointer-events: none;

  background: radial-gradient(
    circle,
    rgba(0, 255, 136, 0.08),
    transparent 70%
  );

  z-index: -1;
}


/* =========================================================
 * 3. 页面 Header
 * ========================================================= */

.blog-header {
  text-align: center;

  margin-bottom: 42px;
}


/*
 * 页面标题
 */
.page-title {
  margin: 0;

  font-size: clamp(30px, 5vw, 52px);

  font-weight: 700;

  /*
   * 荧光绿色。
   */
  color: #00ff88;

  /*
   * 绿色霓虹发光。
   */
  text-shadow:
    0 0 6px rgba(0, 255, 136, 0.6),
    0 0 18px rgba(0, 255, 136, 0.35);

  letter-spacing: 1px;
}


/*
 * Terminal 提示文字。
 */
.terminal-tip {
  margin: 16px 0 0;

  color: #6b8f7a;

  font-size: 14px;
}


/*
 * 终端中的 >
 */
.terminal-prefix {
  color: #00ff88;

  margin-right: 8px;
}


/*
 * 模拟终端光标。
 */
.terminal-cursor {
  color: #00ff88;

  /*
   * 使用动画让光标闪烁。
   */
  animation: cursor-blink 1s infinite;
}


/*
 * 光标闪烁动画。
 */
@keyframes cursor-blink {

  0%,
  50% {
    opacity: 1;
  }

  51%,
  100% {
    opacity: 0;
  }
}


/* =========================================================
 * 4. 搜索区域
 * ========================================================= */

.search-bar {
  display: flex;

  align-items: center;

  gap: 10px;

  margin-bottom: 34px;

  padding: 12px 14px;

  /*
   * 半透明黑色背景。
   */
  background: rgba(8, 14, 12, 0.9);

  /*
   * 绿色终端边框。
   */
  border: 1px solid rgba(0, 255, 136, 0.25);

  border-radius: 8px;

  /*
   * 绿色外发光。
   */
  box-shadow:
    0 0 20px rgba(0, 255, 136, 0.05);

  transition:
    border-color 0.2s ease,
    box-shadow 0.2s ease;
}


/*
 * 搜索框整体获得焦点时，
 * 通过 :focus-within 让整个终端框发光。
 */
.search-bar:focus-within {
  border-color: rgba(0, 255, 136, 0.6);

  box-shadow:
    0 0 20px rgba(0, 255, 136, 0.12);
}


/*
 * 命令行 $
 */
.command-prefix {
  color: #00ff88;

  font-weight: 700;
}


/*
 * 搜索输入框。
 */
.search-input {
  flex: 1;

  height: 40px;

  border: none;

  outline: none;

  background: transparent;

  color: #d8f3dc;

  font-family: inherit;

  font-size: 14px;
}


/*
 * placeholder 使用暗绿色，
 * 避免太抢眼。
 */
.search-input::placeholder {
  color: #426653;
}


/*
 * 搜索按钮。
 */
.search-button {
  height: 38px;

  padding: 0 18px;

  border: 1px solid #00ff88;

  border-radius: 5px;

  background: transparent;

  color: #00ff88;

  font-family: inherit;

  font-size: 13px;

  font-weight: 700;

  cursor: pointer;

  transition:
    background-color 0.2s ease,
    color 0.2s ease,
    box-shadow 0.2s ease;
}


/*
 * Hover 时变成实心荧光按钮。
 */
.search-button:hover {
  background: #00ff88;

  color: #051009;

  box-shadow:
    0 0 15px rgba(0, 255, 136, 0.45);
}


/* =========================================================
 * 5. 加载状态
 * ========================================================= */

.loading-message {
  margin: 20px 0;

  color: #00ff88;

  text-align: center;

  font-size: 14px;

  text-shadow:
    0 0 8px rgba(0, 255, 136, 0.35);
}


.loading-message span {
  margin-right: 8px;
}


/* =========================================================
 * 6. 错误提示
 * ========================================================= */

.error-message {
  margin: 20px 0;

  padding: 12px 16px;

  border: 1px solid rgba(255, 75, 75, 0.4);

  border-radius: 6px;

  background: rgba(90, 10, 10, 0.25);

  color: #ff6b6b;

  font-size: 13px;
}


.error-message span {
  margin-right: 8px;

  font-weight: 700;
}


/* =========================================================
 * 7. 文章列表
 * ========================================================= */

.post-list {
  display: flex;

  flex-direction: column;

  gap: 16px;
}


/*
 * 单篇文章卡片。
 */
.post-item {
  position: relative;

  padding: 24px;

  /*
   * 深灰黑背景。
   */
  background:
    linear-gradient(
      145deg,
      rgba(14, 22, 18, 0.98),
      rgba(7, 11, 9, 0.98)
    );

  /*
   * 非常细的绿色边框。
   */
  border: 1px solid rgba(0, 255, 136, 0.16);

  border-radius: 8px;

  /*
   * 左侧增加一条绿色终端光条。
   */
  overflow: hidden;

  transition:
    border-color 0.2s ease,
    transform 0.2s ease,
    box-shadow 0.2s ease;
}


/*
 * 卡片左侧绿色装饰条。
 */
.post-item::before {
  content: "";

  position: absolute;

  left: 0;
  top: 0;

  width: 3px;
  height: 100%;

  background: #00ff88;

  /*
   * 让它带一点发光效果。
   */
  box-shadow:
    0 0 10px rgba(0, 255, 136, 0.5);

  opacity: 0.7;
}


/*
 * 鼠标悬浮时文章卡片发光。
 */
.post-item:hover {
  transform: translateY(-2px);

  border-color: rgba(0, 255, 136, 0.42);

  box-shadow:
    0 8px 30px rgba(0, 0, 0, 0.4),
    0 0 18px rgba(0, 255, 136, 0.08);
}


/* =========================================================
 * 8. 文章顶部信息
 * ========================================================= */

.post-header {
  display: flex;

  align-items: center;

  justify-content: space-between;

  margin-bottom: 12px;
}


/*
 * 文章 ID。
 */
.post-id {
  margin: 0;

  color: #4f7c62;

  font-size: 11px;

  letter-spacing: 1px;
}


/*
 * 文章在线状态。
 */
.post-status {
  padding: 3px 7px;

  border: 1px solid rgba(0, 255, 136, 0.3);

  border-radius: 3px;

  color: #00ff88;

  font-size: 9px;

  letter-spacing: 1px;

  /*
   * 稍微增加状态发光效果。
   */
  text-shadow:
    0 0 6px rgba(0, 255, 136, 0.4);
}


/* =========================================================
 * 9. 文章标题
 * ========================================================= */

.post-title {
  margin: 0 0 12px;

  font-size: clamp(20px, 3vw, 26px);

  line-height: 1.5;

  font-weight: 700;

  color: #eafff1;

  /*
   * 标题轻微绿色发光。
   */
  text-shadow:
    0 0 8px rgba(0, 255, 136, 0.08);
}


/* =========================================================
 * 10. 摘要
 * ========================================================= */

.post-summary {
  margin: 0 0 20px;

  color: #7da18a;

  font-size: 14px;

  line-height: 1.8;

  /*
   * 最多显示两行。
   */
  display: -webkit-box;

  -webkit-box-orient: vertical;

  -webkit-line-clamp: 2;

  overflow: hidden;
}


/* =========================================================
 * 11. 文章底部信息
 * ========================================================= */

.post-meta {
  display: flex;

  align-items: center;

  justify-content: space-between;

  padding-top: 16px;

  border-top: 1px dashed rgba(0, 255, 136, 0.12);
}


/*
 * 阅读量。
 */
.post-views {
  color: #557866;

  font-size: 11px;

  letter-spacing: 1px;
}


/* =========================================================
 * 12. 详情按钮
 * ========================================================= */

.detail-link {
  display: inline-flex;

  align-items: center;

  justify-content: center;

  height: 32px;

  padding: 0 13px;

  border: 1px solid rgba(0, 255, 136, 0.35);

  border-radius: 4px;

  background: rgba(0, 255, 136, 0.03);

  color: #00ff88;

  text-decoration: none;

  font-size: 11px;

  font-weight: 700;

  letter-spacing: 1px;

  transition:
    background-color 0.2s ease,
    color 0.2s ease,
    box-shadow 0.2s ease;
}


/*
 * Hover 后变成绿色霓虹按钮。
 */
.detail-link:hover {
  background: #00ff88;

  color: #051009;

  box-shadow:
    0 0 15px rgba(0, 255, 136, 0.3);
}


/* =========================================================
 * 13. 分页
 * ========================================================= */

.pagination {
  display: flex;

  align-items: center;

  justify-content: center;

  gap: 14px;

  margin-top: 34px;

  padding-top: 20px;

  border-top: 1px dashed rgba(0, 255, 136, 0.12);
}


/*
 * 分页按钮。
 */
.pagination-button {
  height: 34px;

  padding: 0 14px;

  border: 1px solid rgba(0, 255, 136, 0.25);

  border-radius: 4px;

  background: transparent;

  color: #7da18a;

  font-family: inherit;

  font-size: 11px;

  cursor: pointer;

  transition:
    color 0.2s ease,
    border-color 0.2s ease,
    background-color 0.2s ease;
}


/*
 * 分页按钮 Hover。
 */
.pagination-button:hover {
  border-color: #00ff88;

  color: #00ff88;

  background: rgba(0, 255, 136, 0.05);
}


/*
 * 当前页信息。
 */
.pagination-info {
  color: #557866;

  font-size: 11px;

  letter-spacing: 1px;
}


/*
 * 当前页数字突出显示。
 */
.pagination-current {
  color: #00ff88;

  font-weight: 700;

  text-shadow:
    0 0 8px rgba(0, 255, 136, 0.4);
}


/* =========================================================
 * 14. 页脚
 * ========================================================= */

.blog-footer {
  display: flex;

  align-items: center;

  justify-content: space-between;

  margin-top: 40px;

  padding-top: 18px;

  border-top: 1px solid rgba(0, 255, 136, 0.08);

  color: #355441;

  font-size: 10px;

  letter-spacing: 1px;
}


/*
 * 状态文字增加一点绿色。
 */
.blog-footer span:last-child {
  color: #47735a;
}


/* =========================================================
 * 15. 手机端适配
 * ========================================================= */

@media (max-width: 600px) {

  /*
   * 缩小整体左右间距。
   */
  .cyber-blog {
    padding: 32px 14px 28px;
  }


  /*
   * 缩小标题。
   */
  .page-title {
    font-size: 30px;
  }


  /*
   * 移动端搜索按钮缩小。
   */
  .search-button {
    padding: 0 12px;

    font-size: 11px;
  }


  /*
   * 移动端文章卡片缩小内边距。
   */
  .post-item {
    padding: 18px;
  }


  /*
   * 标题缩小。
   */
  .post-title {
    font-size: 19px;
  }


  /*
   * 页脚改成上下排列，
   * 防止手机宽度不足。
   */
  .blog-footer {
    flex-direction: column;

    align-items: flex-start;

    gap: 8px;
  }

}

</style>
