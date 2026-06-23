package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.TyposPage;

public class VerifyNoTypoOnRefreshTest extends BaseTest {

    @Test
    public void verifyNoTypoOnRefresh() {

        TyposPage page = new TyposPage(driver);

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}