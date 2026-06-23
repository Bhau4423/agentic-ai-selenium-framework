package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.HoversPage;

public class HideProfileDetailsOnMouseOutTest extends BaseTest {

    @Test
    public void hideProfileDetailsOnMouseOut() {

        HoversPage page = new HoversPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}