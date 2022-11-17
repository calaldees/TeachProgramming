describe('Google', () => {
	it('Search for university webpage and check university logo is present', () => {
		cy.visit("https://www.google.co.uk?&hl=en&lr=lang_en")
		// * Perform a google search for canterbury christ church university (with a spelling mistake)
		cy.get('button').contains("Accept all").scrollIntoView().should('be.visible').click()
		cy.get('input[title="Search"]').should('be.visible').type("Canterbury christ chcurch uni{enter}")
		// * Check that `canterbury.ac.uk` is somewhere in the returned list of searches
		cy.contains("canterbury.ac.uk").click()
		// * Follow the google search link to the main university webpage and check the logo is visible
		cy.get("#onetrust-accept-btn-handler").click()
		cy.get('img[alt="Canterbury Christ Church University Logo"]').should('be.visible')
		// * Hint: "Accept Cookie" buttons will block your way. Your test should deal with these
	});
});
/*
* Run with
    * Local Headless: `npx cypress run --spec cypress/google.spec.cy.js`
    * Container Headless: `make cypress_cmd CYPRESS_CMD="run --spec cypress/google.spec.cy.js"`
* https://docs.cypress.io/api/commands/
    * `.visit("https://site")`
    * `.contains("text on webpage")`
    * `.click()`
    * `.type("the text you want to type{enter}")`
    * `.get('???')`
        * `.get('input[title="???"]')`
        * `.get('#id_of_element')`
        * `.get('img[alt="???"')`
    * `.should('be.visible')`
	* `.scrollIntoView()`
*/