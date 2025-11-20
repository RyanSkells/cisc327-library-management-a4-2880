from playwright.sync_api import Page, expect

def test_add_book_workflow(page: Page):
    page.goto("http://localhost:5000/")

    #Click button
    page.get_by_role(role="link", name="Add Book").click()

    #Check that all input fields and 'add book' button are present
    expect(page.get_by_role(role="textbox", name="Title")).to_be_visible()
    expect(page.get_by_role(role="textbox", name="Author")).to_be_visible()
    expect(page.get_by_role(role="textbox", name="ISBN")).to_be_visible()
    expect(page.get_by_role(role="spinbutton", name="Total Copies")).to_be_visible()
    expect(page.get_by_role(role="button", name="Add Book to Catalog")).to_be_visible()

    #Fill in input fields
    page.get_by_role(role="textbox", name="Title").fill("Test Title")
    page.get_by_role(role="textbox", name="Author").fill("Test Author")
    page.get_by_role(role="textbox", name="ISBN").fill("1234567890123")
    page.get_by_role(role="spinbutton", name="Total Copies").fill("5")

    #Click the add book button
    page.get_by_role(role="button", name="Add Book to Catalog").click()

    #Check that we were redirected to the catalog page
    expect(page.get_by_role(role="heading", name="📖 Book Catalog"))

    #Check that a book with the test title is present
    expect(page.get_by_role(role="cell", name="Test Title"))

def test_borrow_return_book_workflow(page: Page):
    page.goto("http://localhost:5000/")

    #Find input fields on page
    table_body = page.get_by_role(role="table").locator('tbody')
    action_cell = table_body.locator('tr').nth(1).locator('td').nth(5) #The test book from previous test case

    #Cell found, borrow the book
    action_cell.get_by_role(role="textbox", name="Patron ID (6 Digits)").fill("456789")
    action_cell.get_by_role(role="button", name="Borrow").click()

    #Find success message
    expect(page.get_by_text("Successfully borrowed")).to_be_visible()

    #Navigate to returning menu, and check that necessary  UI elements are loaded
    page.get_by_role(role="link", name="↩️ Return Book").click()
    expect(page.get_by_role(role="textbox", name="Patron ID *")).to_be_visible()
    expect(page.get_by_role(role="spinbutton", name="Book ID *")).to_be_visible()
    expect(page.get_by_role(role="button", name="Process Return")).to_be_visible()

    #Fill out input fields
    page.get_by_role(role="textbox", name="Patron ID *").fill("456789")
    page.get_by_role(role="spinbutton", name="Book ID *").fill("4")
    page.get_by_role(role="button", name="Process Return").click()

    #Look for confirmation message
    expect(page.get_by_text("Fee amount:")).to_be_visible()
