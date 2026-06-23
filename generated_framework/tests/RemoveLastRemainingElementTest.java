package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.AddRemoveElementsPage;

public class RemoveLastRemainingElementTest extends BaseTest {

    @Test
    public void removeLastRemainingElement() {

        AddRemoveElementsPage page = new AddRemoveElementsPage(driver);

        wait.until(ExpectedConditions.elementToBeClickable(page.get_Add_Element()));
        page.get_Add_Element().click();

        Assert.assertTrue(driver.getCurrentUrl().contains("dashboard"));

    }

}