package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.DynamicContentPage;

public class EnableStaticContentTest extends BaseTest {

    @Test
    public void enableStaticContent() {

        DynamicContentPage page = new DynamicContentPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}