import frappe
from airplane_mode.airplane_mode.doctype.knowledge_article.search.knowledge_article_search import KnowledgeArticleSearch


@frappe.whitelist()
def secure_search(text):
    search = KnowledgeArticleSearch("knowledge_articles")
    indexed_results = search.search(text, limit=50)

    # permitted_names = set(
    #     frappe.get_list(
    #         "Knowledge Article",
    #         filters={
    #             "name": ["in", [r.name for r in indexed_results]],
    #             "published": 1,
    #         },
    #         pluck="name",
    #     )
    # )

    # return [
    #     result
    #     for result in indexed_results
    #     if result.name in permitted_names
    # ][:20]

    return [
        result
        for result in indexed_results
    ]
