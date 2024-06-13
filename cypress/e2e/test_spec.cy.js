import "cypress-real-events/support";

describe('template spec', () => {
  it('passes', () => {
    cy.visit('https://www.hiredscore.com')
    cy.contains("div", "About").realHover('mouse')
    cy.contains("a", "Careers").click()
    cy.url().should('include', 'https://www.hiredscore.com/careers')
    cy.contains("div", "Group Manager - Program Implementations").click()
    cy.url().should('include', 'https://www.hiredscore.com/career-details?position=B1.64E', {force: true})
    cy.go('back')
    cy.contains("div", "Resources").click()
    cy.contains("span", "Press & Awards").click()
    cy.url().should('include', 'https://www.hiredscore.com/resources?type=Press+%26+Awards')
    var texts = []
    cy.get('p[class="resources-card_headline"]')
    .each(($ele) => {
      texts.push($ele.text().trim())
    })
    .then(() =>{
      cy.writeFile('1.txt', texts.join("\n"));
    })
  })
})

