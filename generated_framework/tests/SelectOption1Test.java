package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.DropdownPage;

public class SelectOption1Test extends BaseTest {

    @Test
    public void selectOption1() {

        DropdownPage page = new DropdownPage(driver);

        wait.until(ExpectedConditions.visibilityOf(page.get_dropdown()));
        // TODO: Select value for dropdown

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}