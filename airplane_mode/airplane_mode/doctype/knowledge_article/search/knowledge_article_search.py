import frappe
from frappe.search.full_text_search import FullTextSearch
from whoosh.fields import Schema, ID, TEXT

# =============================================================
# bench --site my-airplane-mode.local console

# from airplane_mode.airplane_mode.doctype.knowledge_article.search.knowledge_article_search import KnowledgeArticleSearch
# article_search = KnowledgeArticleSearch("knowledge_articles")
# article_search.build()
# =============================================================
# results = article_search.search(
#     "Application Programming",
#     limit=10,
# )
# for result in results:
#     print(result.name)
#     print(result.title)
#     print(result.content_highlights)


class KnowledgeArticleSearch(FullTextSearch):
    def get_schema(self):
        """
        Define the structure of one document in the search index.
        stored=True means the original value can be returned in the search result.
        """
        return Schema(
            name=ID(stored=True),
            title=TEXT(stored=True),
            content=TEXT(stored=True),
            category=ID(stored=True),
        )

    def get_id(self):
        """
        Field that uniquely identifies an indexed document.
        """
        return "name"

    def get_fields_to_search(self):
        """
        Fields searched when search() is called.
        Title comes first, so Frappe gives it a higher search weight than content.
        """
        return ["title", "content"]

    def get_items_to_index(self):
        """
        Return all documents when building the complete index.
        """
        articles = frappe.get_all(
            "Knowledge Article",
            filters={"published": 1},
            fields=["name", "title", "content", "category"],
        )

        return [
            frappe._dict(
                name=article.name,
                title=article.title or "",
                content=article.content or "",
                category=article.category or "",
            )
            for article in articles
        ]

    def get_document_to_index(self, name):
        """
        Return one document when updating a single index entry.
        """
        article = frappe.db.get_value(
            "Knowledge Article",
            {"name": name, "published": 1},
            ["name", "title", "content", "category"],
            as_dict=True,
        )

        if not article:
            return None

        return frappe._dict(
            name=article.name,
            title=article.title or "",
            content=article.content or "",
            category=article.category or "",
        )

    def parse_result(self, result):
        """
        Convert a Whoosh result into the application's output format.
        """
        return frappe._dict(
            name=result["name"],
            title=result["title"],
            category=result["category"],
            title_highlights=result.highlights("title"),
            content_highlights=result.highlights("content"),
        )
