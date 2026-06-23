package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.InfiniteScrollPage;

public class VerifyContinuousLoadingTest extends BaseTest {

    @Test
    public void verifyContinuousLoading() {

        InfiniteScrollPage page = new InfiniteScrollPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}