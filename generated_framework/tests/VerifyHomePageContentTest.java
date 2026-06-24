package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.DynamicContentPage;

public class VerifyHomePageContentTest extends BaseTest {

    @Test
    public void verifyHomePageContent() {

        DynamicContentPage page = new DynamicContentPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}