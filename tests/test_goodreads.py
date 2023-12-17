import unittest
from BaseTest import BaseTest
from faker import Faker
from pages.MyBooks import MyBooks
from pages.SearchBook import SearchBook

class TestGoodreads(BaseTest):

     def test_search_book_by_ISBN(self):
          expected_text = 'Memórias Póstumas de Brás Cubas'
          isbn='9786586040920'
          SearchBook.searchByText(self,isbn)
          SearchBook.openBook(self)
          resultado = SearchBook.checkBookTitle(self,expected_text)
          self.assertTrue(resultado, "O texto do elemento não corresponde ao esperado.")

     def test_search_book_by_title(self):
          expected_text = 'O Homem que Odiava Machado de Assis'
          title = 'O Homem que Odiava Machado de Assis'
          SearchBook.searchByText(self,title)
          SearchBook.openBook(self)
          resultado = SearchBook.checkBookTitle(self,expected_text)
          self.assertTrue(resultado, "O texto do elemento não corresponde ao esperado.")

     def test_search_book_by_author(self):
          expected_text = 'Wuthering Heights'
          author = 'Emily Bronte'
          SearchBook.searchByText(self,author)
          SearchBook.openBook(self)
          resultado = SearchBook.checkBookTitle(self,expected_text)
          self.assertTrue(resultado, "O texto do elemento não corresponde ao esperado.")

     def test_create_new_bookshelf(self):
         MyBooks.openMyBooks(self)
         bookshelfName = 'my-new-bookshelf'
         MyBooks.createBookshelf(self,bookshelfName)
         assert MyBooks.isSucessMessageVisible(self), "A mensagem de sucesso não está visível!"
         MyBooks.deleteBookshelf(self,bookshelfName)

     def test_create_new_tag(self):
          MyBooks.openMyBooks(self)
          fake = Faker()
          fake_name = fake.name()
          tagName = 'My New Tag:' + fake_name
          MyBooks.createTag(self,tagName)
          assert MyBooks.isSucessMessageVisible(self), "A mensagem de sucesso não está visível!"
      
     def test_add_tag_to_book(self):
          #cria tag
          MyBooks.openMyBooks(self)
          tagName = 'My New Tag'
          MyBooks.createTag(self,tagName)
          #busca livro
          SearchBook.searchByText(self,'Dom Casmurro')
          SearchBook.openBook(self)
          #add tag no livro
          MyBooks.addTag(self,tagName)
          #assert
          MyBooks.openMyBooks(self)
          MyBooks.openTag(self)
          resultado = SearchBook.checkBookTitleTagOrBookshelf(self,"Dom Casmurro")
          self.assertTrue(resultado, "O texto do elemento não corresponde ao esperado.")
          #deleta sujeira no app
          MyBooks.deleteTagWithBook(self)
     
     def test_add_book_to_bookshelf(self):
          #cria bookshelf
          MyBooks.openMyBooks(self)
          bookshelfName = 'my-new-bookshelf'
          MyBooks.createBookshelf(self,bookshelfName)
          #busca livro
          SearchBook.searchByText(self,'Dom Casmurro')
          SearchBook.openBook(self)
          #add livro na estante
          MyBooks.addBookshelf(self,bookshelfName)
          #assert
          MyBooks.openMyBooks(self)
          MyBooks.openBookshelf(self,bookshelfName)
          resultado = SearchBook.checkBookTitleTagOrBookshelf(self,'Dom Casmurro')
          self.assertTrue(resultado, "O texto do elemento não corresponde ao esperado.")
          #deleta sujeira no app
          MyBooks.deleteBookshelfWithBook(self,bookshelfName)
          
if __name__ == '__main__':
     unittest.main()