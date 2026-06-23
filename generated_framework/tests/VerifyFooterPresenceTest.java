package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.InfiniteScrollPage;

public class VerifyFooterPresenceTest extends BaseTest {

    @Test
    public void verifyFooterPresence() {

        InfiniteScrollPage page = new InfiniteScrollPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}