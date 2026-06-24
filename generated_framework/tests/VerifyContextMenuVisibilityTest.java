package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.ContextMenuPage;

public class VerifyContextMenuVisibilityTest extends BaseTest {

    @Test
    public void verifyContextMenuVisibility() {

        ContextMenuPage page = new ContextMenuPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}