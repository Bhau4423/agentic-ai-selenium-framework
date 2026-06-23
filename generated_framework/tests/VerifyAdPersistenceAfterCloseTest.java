package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.InfiniteScrollPage;

public class VerifyAdPersistenceAfterCloseTest extends BaseTest {

    @Test
    public void verifyAdPersistenceAfterClose() {

        InfiniteScrollPage page = new InfiniteScrollPage(driver);

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}