Given(/^Open sidebar$/) do
  wait_for_element_exists("KVSideBarHamburgerView", timout:5)
  uia_tap_mark "sidebar_menu_button"
end

When(/^I clcik the setting button$/) do
  scroll("UITableView", :down)
  uia_tap_mark("設定")
end

Then(/^I go to setting page$/) do
  begin
    wait_for_element_exists("UITableViewLabel {text CONTAINS 'ID'}", timeout: 5)
  rescue Calabash::Cucumber::WaitHelpers::WaitError => e
    puts(e)
  end
end

