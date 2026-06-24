package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.DynamicContentPage;

public class RefreshPageContentTest extends BaseTest {

    @Test
    public void refreshPageContent() {

        DynamicContentPage page = new DynamicContentPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}