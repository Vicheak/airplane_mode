import frappe


def queue_article_update(doc, method=None):
    frappe.enqueue(
        "airplane_mode.airplane_mode.doctype.knowledge_article.search.knowledge_article_indexing.update_article",
        queue="short",
        article_name=doc.name,
    )


def queue_article_removal(doc, method=None):
    frappe.enqueue(
        "airplane_mode.airplane_mode.doctype.knowledge_article.search.knowledge_article_indexing.remove_article",
        queue="short",
        article_name=doc.name,
    )


def update_article(article_name):
    from airplane_mode.airplane_mode.doctype.knowledge_article.search.knowledge_article_search import KnowledgeArticleSearch

    search = KnowledgeArticleSearch("knowledge_articles")

    published = frappe.db.get_value(
        "Knowledge Article",
        article_name,
        "published",
    )

    if published:
        search.update_index_by_name(article_name)
    else:
        search.remove_document_from_index(article_name)


def remove_article(article_name):
    from airplane_mode.airplane_mode.doctype.knowledge_article.search.knowledge_article_search import KnowledgeArticleSearch

    search = KnowledgeArticleSearch("knowledge_articles")
    search.remove_document_from_index(article_name)
