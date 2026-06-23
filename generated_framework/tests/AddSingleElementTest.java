package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.AddRemoveElementsPage;

public class AddSingleElementTest extends BaseTest {

    @Test
    public void addSingleElement() {

        AddRemoveElementsPage page = new AddRemoveElementsPage(driver);

        wait.until(ExpectedConditions.elementToBeClickable(page.get_Add_Element()));
        page.get_Add_Element().click();

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}