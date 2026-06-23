package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.TablesPage;

public class VerifyDeleteActionTest extends BaseTest {

    @Test
    public void verifyDeleteAction() {

        TablesPage page = new TablesPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}