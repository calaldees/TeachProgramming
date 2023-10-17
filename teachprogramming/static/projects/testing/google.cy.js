describe('Google', () => {
	it('Search for university webpage and check university logo is present', () => {
		cy.visit("https://www.google.co.uk?&hl=en&lr=lang_en")
		// * Perform a google search for canterbury christ church university (with a spelling mistake)
		cy.get('button').contains("Accept all").scrollIntoView().should('be.visible').click()
		cy.get('textarea[title="Search"]').should('be.visible').type("Canterbury christ chcurch uni{enter}")
		// * Check that `canterbury.ac.uk` is somewhere in the returned list of searches
		cy.contains("canterbury.ac.uk").should('be.visible').click()
		// * Follow the google search link to the main university webpage and check the logo is visible
		cy.get("#onetrust-accept-btn-handler").click()
		cy.get('img[alt="Canterbury Christ Church University Logo"]').should('be.visible')
		// * Hint: "Accept All Cookies" buttons will block your way. Your test should deal with this - interestingly there are multiple "Accept All Cookies" buttons, use the id with the css selection `#` to find the correct one
	})
})
/*
* Run with
	* With GUI: `npx cypress open`
	* Local Headless: `npx cypress run --spec cypress/google.spec.cy.js`
	* Container Headless: `make cypress_cmd CYPRESS_CMD="run --spec cypress/google.spec.cy.js"`
* https://docs.cypress.io/api/table-of-contents
	* `.visit("https://site")`
	* `.contains("text on webpage")`
	* `.scrollIntoView()`
	* `.should('be.visible')`
	* `.click()`
	* `.type("the text you want to type{enter}")`
	* `.get('???')`
		* `.get('input[title="???"]')`
		* `.get('#id_of_element')`
		* `.get('img[alt="???"')`
*/