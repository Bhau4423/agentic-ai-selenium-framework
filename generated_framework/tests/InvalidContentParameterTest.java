package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.DynamicContentPage;

public class InvalidContentParameterTest extends BaseTest {

    @Test
    public void invalidContentParameter() {

        DynamicContentPage page = new DynamicContentPage(driver);

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}