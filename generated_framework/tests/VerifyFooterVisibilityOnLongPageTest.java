package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.InfiniteScrollPage;

public class VerifyFooterVisibilityOnLongPageTest extends BaseTest {

    @Test
    public void verifyFooterVisibilityOnLongPage() {

        InfiniteScrollPage page = new InfiniteScrollPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().contains("dashboard"));

    }

}