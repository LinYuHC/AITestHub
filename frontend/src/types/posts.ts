export interface PostListItem{
    id: number;
    // 标题
    title: string;
    // 摘要
    summary: string;
    // 分类
    category: string;
    // 封面图
    cover_image?: string;
    // 阅读量
    views_count: number;
    // 作者
    author_id: number;
}
export interface CreatePostRequest {
    // 创建博客数据模型
    // 标题
    title: string;
    // 摘要
    summary: string;
    // 内容
    content: string;
    // 状态：1 - 已发布，2 - 草稿 3删除
    status: number;
    // 分类ID，可选
    category_id?: number;
    // 封面图,可选
    cover_image?: string;
    // 是否允许评论，默认true
    allow_comment: boolean;
    // 是否置顶,默认false
    is_top: boolean;
}
export interface PostDetail {
    id: number;
    // 标题
    title: string;
    // 摘要
    summary: string;
    // 分类
    category_id: number;
    // 封面图
    cover_image?: string;
    // 阅读量
    views_count: number;
    // 作者
    author_id: number;
    // 内容
    content: string;
}
export interface PostsListData {
  total: number
  items: PostListItem[]
}

export interface ResponseModel<T> {
    /*
    表示：
    后端统一返回结构。
    这个 T 是 TypeScript 的泛型，今天先知道它是“把具体 data 类型传进去”即可。
    */
  code: number
  message: string
  data: T
}